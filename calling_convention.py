# Copyright 2020 Katharina Utz <katharina.utz@stud.uni-due.de>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from binaryninja import CallingConvention


class DefaultCallingConvention(CallingConvention):
    name = "default"
    int_arg_regs = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']
    int_return_reg = 'a0'
    high_int_return_reg = 'a1'
