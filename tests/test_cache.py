# 3rd party
import pytest

# this package
from seed_intersphinx_mapping.cache import Cache, posargs2kwargs


def demo_function(arg1, arg2, arg3):
	pass


@pytest.mark.parametrize(
		"args, posarg_names, kwargs, expects",
		[
				((1, 2, 3), ("arg1", "arg2", "arg3"), {}, {"arg1": 1, "arg2": 2, "arg3": 3}),
				((1, 2, 3), ("arg1", "arg2", "arg3"), None, {"arg1": 1, "arg2": 2, "arg3": 3}),
				((1, 2, 3), ("arg1", "arg2", "arg3"), {"arg4": 4}, {"arg1": 1, "arg2": 2, "arg3": 3, "arg4": 4}),
				((1, 2, 3), demo_function, None, {
						"arg1": 1,
						"arg2": 2,
						"arg3": 3,
						}),
				]
		)
def test_posargs2kwargs(args, posarg_names, kwargs, expects):
	assert posargs2kwargs(args, posarg_names, kwargs) == expects


@pytest.fixture(scope="session")
def testing_cache():
	cache = Cache("testing_seed_intersphinx_mapping")
	assert cache.clear()
	yield cache
	assert cache.clear()


@pytest.mark.parametrize("run_number", [1, 2])
def test_cache(testing_cache, capsys, run_number):

	@testing_cache
	def cached_function(arg1: int, arg2: float, arg3: str):
		print("Running")
		return (arg1**int(arg2)) * arg3

	assert not (testing_cache.cache_dir / "cached_function.json").is_file()

	assert cached_function(2, 5.5, "☃") == "☃" * 32
	assert (testing_cache.cache_dir / "cached_function.json").is_file()

	for i in range(10):
		assert cached_function(2, 5.5, "☃") == "☃" * 32

	assert cached_function(2, 5.8, "☃") == "☃" * 32

	captured = capsys.readouterr()
	assert captured.out == "Running\nRunning\n"

	assert testing_cache.clear(cached_function)
	assert not (testing_cache.cache_dir / "cached_function.json").is_file()
	assert testing_cache.cache_dir.is_dir()

	assert cached_function(2, 5.5, "☃") == "☃" * 32
	capsys.readouterr()  # prevents the above call polluting stdout

	old_id = id(cached_function)

	@testing_cache  # type: ignore
	def cached_function(arg1: int, arg2: float, arg3: str):  # type: ignore
		print("Running 2nd function")
		return (arg1**int(arg2)) * arg3

	assert id(cached_function) != old_id

	assert cached_function(2, 5.5, "☃") == "☃" * 32
	assert (testing_cache.cache_dir / "cached_function.json").is_file()
	assert testing_cache.clear(cached_function)

	captured = capsys.readouterr()
	# if the cache wasn't working this would be "Running 2nd function\n"
	assert captured.out == ""
