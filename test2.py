#test2.py

from dataclasses import dataclass
from typing import ClassVar, List

@dataclass
class Ex:
    SLCPS: ClassVar[List[str]] = ['bt_soc_thunderboard_brd4166a','bt_soc_thunderboard_brd4184a','bt_soc_thunderboard_brd4184b','bt_soc_xg24_dev_kit_brd2601b']
    PROJS: ClassVar[List[str]] = ['bt_soc_thunderboard/']
    slcp: str
    proj: str
@property
def file_name(self):
       return print(str(self)+'.slcp')

def _str_(self):
    return print(f'{self.slcp} of {self.proj}')
def _format_(self,format):
        return print(f'{str(self):{format}}')
