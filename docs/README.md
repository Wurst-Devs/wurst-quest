# DOCS

* [Architecture](#architecture)
  * [General Workflow](#general-workflow)
  * [Game States](#game-states)
* [Developer guide](#developer-guide)
  * [Coding](#coding)
    * [1. Use Typing](#1-use-typing)
    * [2. Naming and case](#2-naming-and-case)
    * [3. Imports and sub-modules](#3-imports-and-sub-modules)
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

**wrong**
	
```python
class NameClass:
	def __init__(self, name):
		self.name = name
	
	def get_prefixed(self, prefix=""):
		return f"{prefix} {self.name}".strip()
	
	def get_chars(self):
		return self.name.split("")

```
	
**good**
	
```python
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
	
**wrong**
	
```python
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
	
	def getPrefixed(self, p: str="") -> str:
		return f"{p} {self.get()}".strip()
```
	
**good**
	
```python
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

#### 3. Imports and sub-modules

* Import only classes and functions used
* Relative sub-modules should be access through dot: `from .<sub>.<subsub> import Class`
* Relative cross-modules should be access through all hierarchy: `from <top-level>.<othersub> import Class`
* Sub-modules should expose classes through their `__init__.py`
* Subsequently, a module calling  another should not access its files directly

<details><summary>Sample code (click)</summary>
<p>

files:
```
└─ src
   └─ wurst_quest
      ├─ __init__.py
      ├─ core
      │  ├─ __init__.py
      │  ├─ class1.py
      │  └─ models
      │     ├─ __init__.py
      │     └─ class2.py
      └─ utils
         ├─ __init__.py
         └─ utils.py
```

**wrong**

`src/wurst_quest/core/class1.py`
```python
from .models.class2 import *

def Class1:
	def __init__(self) -> None:
		self.class2 = Class2()
```
`src/wurst_quest/core/models/class2.py`
```python
from ...utils.utils import *

def Class2:
	def __init__(self) -> None:
		util_function()
```
`src/wurst_quest/utils/utils.py`
```python
def util_function():
	pass
```
**good**

`src/wurst_quest/core/__init__.py`
```python
from .class1 import Class1
```
`src/wurst_quest/core/class1.py`
```python
from .models import Class2

def Class1:
	def __init__(self) -> None:
		self.class2 = Class2()
```
`src/wurst_quest/core/models/__init__.py`
```python
from .class2 import Class2
```
`src/wurst_quest/core/models/class2.py`
```python
from wurst_quest.utils import util_function

def Class2:
	def __init__(self) -> None:
		util_function()
```
`src/wurst_quest/utils/__init__.py`
```python
from .utils import util_function
```
`src/wurst_quest/utils/utils.py`
```python
def util_function():
	pass
```

</p>
</details>

### Testing

TODO

### Gitting

TODO

### Reviewing

TODO
