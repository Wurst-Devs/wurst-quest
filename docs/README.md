# DOCS

* [Architecture](#architecture)
  * [General Workflow](#general-workflow)
  * [Game States](#game-states)
* [Developer guide](#developer-guide)
  * [Coding](#coding)
    * [1. Use Typing](#1-use-typing)
    * [2. Naming and case](#2-naming-and-case)
  * [Testing](#testing)
  * [Gitting](#gitting)
  * [Reviewing](#reviewing)

## Architecture

### General Workflow

![](./diagrams/general_workflow.png)

### Game States

![](./diagrams/game_states.png)

## Developer Guide

### Coding

#### 1. Use Typing

* For arguments of functions
* For return type of functions
* Use complex typing when possible, ex: `Tuple[List[str], int]`

<details><summary>Sample code (click)</summary>
<p>

```python
# wrong
class NameClass:
	def __init__(self, name):
		self.name = name
	
	def get_prefixed(self, prefix=""):
		return f"{prefix} {self.name}".strip()
	
	def get_chars(self):
		return self.name.split("")

#  good
from typing import List

class NameClass:
	def __init__(self, name: str) -> None:
		self.name = name
	
	def get_prefixed(self, prefix: str="") -> str:
		return f"{prefix} {self.name}".strip()
	
	def get_chars(self) -> List[str]:
		return self.name.split("")
```

</p>
</details>

#### 2. Naming and case

* CamelCase for classes
* snake_case for attributes and functions
* `_` prefixed for protected attributes/functions (inherited)
* `__` prefixed for private attributes/functions (not inherited)
* Don't hesitate to be verbose (ex: `monster_name_list` instead of `mnl`)
  
<details><summary>Sample code (click)</summary>
<p>

```python
# wrong
from typing import List, Any

class Value_Class:
	def __init__(self, v: Any) -> None:
		self.v = None

	def get(self) -> Any:
		return self.v

	def set(self, v: Any) -> None:
		self.v = v


class Name_Class(Value_Class):
	def __init__(self, Name: str) -> None:
		super().__init__(Name)
	
	def get_prefixed(self, p: str="") -> str:
		return f"{p} {self.get()}".strip()

# good
from typing import List, Any

class ValueClass:
	def __init__(self, value: Any) -> None:
		self.__internal_value = None

	def _get_value(self) -> Any:
		return self.__internal_value

	def _set_value(self, value: Any) -> None:
		self.__internal_value = value


class NameClass(ValueClass):
	def __init__(self, name: str) -> None:
		super().__init__(name)
	
	def get_prefixed(self, prefix: str="") -> str:
		return f"{prefix} {self._get_value()}".strip()
```
</p>
</details>


### Testing

TODO

### Gitting

TODO

### Reviewing

TODO
