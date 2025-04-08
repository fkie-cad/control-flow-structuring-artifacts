// rev.ng version 6465a75

_ABI(SystemV_x86_64)
void test_1(generic64_t argument_0) {
    struct _PACKED struct_69 {
        uint8_t padding_at_0[12];
        generic32_t offset_12;
        uint8_t padding_at_16[8];
    } _stack;
    int32_t _var_0;
    int32_t _var_1;
    _stack.offset_12 = (number32_t) argument_0;
    _var_1 = printf_((const int8_t *) "Block 1");
    if ((int32_t) _stack.offset_12 > (int32_t) 6) {
        if (_stack.offset_12 == 125) {
            int32_t _var_2;
            _var_2 = printf_((const int8_t *) "Block 7");
        } else {
            _var_0 = printf_((const int8_t *) "Block 8");
        }
    } else {
        if (!(_stack.offset_12 < 2 || _stack.offset_12 > 6)) {
            __abort("A longjmp was taken");
        }
        _var_0 = printf_((const int8_t *) "Block 8");
    }
    int32_t _var_3;
    _var_3 = printf_((const int8_t *) "Block 9");
}

_ABI(SystemV_x86_64) _Noreturn
void function_0x40117b_Code_x86_64(void) {
    int32_t _var_0;
    int32_t _var_1;
    _var_1 = printf_((const int8_t *) "Block 2");
    _var_0 = printf_((const int8_t *) "Block 9");
    __abort("A longjmp was taken");
}

_ABI(SystemV_x86_64) _Noreturn
void function_0x40118c_Code_x86_64(void) {
    int32_t _var_0;
    int32_t _var_1;
    _var_1 = printf_((const int8_t *) "Block 3");
    _var_0 = printf_((const int8_t *) "Block 9");
    __abort("A longjmp was taken");
}

_ABI(SystemV_x86_64) _Noreturn
void function_0x40119d_Code_x86_64(void) {
    int32_t _var_0;
    int32_t _var_1;
    _var_1 = printf_((const int8_t *) "Block 4");
    _var_0 = printf_((const int8_t *) "Block 9");
    __abort("A longjmp was taken");
}

_ABI(SystemV_x86_64) _Noreturn
void function_0x4011ae_Code_x86_64(void) {
    int32_t _var_0;
    int32_t _var_1;
    _var_1 = printf_((const int8_t *) "Block 5");
    _var_0 = printf_((const int8_t *) "Block 9");
    __abort("A longjmp was taken");
}

_ABI(SystemV_x86_64) _Noreturn
void function_0x4011bf_Code_x86_64(void) {
    int32_t _var_0;
    int32_t _var_1;
    _var_1 = printf_((const int8_t *) "Block 6");
    _var_0 = printf_((const int8_t *) "Block 9");
    __abort("A longjmp was taken");
}



_ABI(SystemV_x86_64)
generic64_t test_2(generic64_t argument_0, generic64_t argument_1) {
    struct _PACKED struct_70 {
        uint8_t padding_at_0[8];
        generic32_t offset_8;
        generic32_t offset_12;
        uint8_t padding_at_16[8];
    } _stack;
    int32_t _var_0;
    _stack.offset_12 = (number32_t) argument_0;
    _stack.offset_8 = (number32_t) argument_1;
    _var_0 = printf_((const int8_t *) "Block 1");
    if ((_stack.offset_12 == 1) && (_stack.offset_8 == 1)) {
        int32_t _var_1;
        _var_1 = printf_((const int8_t *) "Block 3");
    } else {
        int32_t _var_2;
        _var_2 = printf_((const int8_t *) "Block 2");
    }
    if (_stack.offset_12 == 1) {
        int32_t _var_3;
        _var_3 = printf_((const int8_t *) "Block 5");
    } else {
        int32_t _var_4;
        _var_4 = printf_((const int8_t *) "Block 4");
    }
    int32_t _var_5;
    _var_5 = printf_((const int8_t *) "Block 6");
    return 0;
}



_ABI(SystemV_x86_64)
void test_3(generic64_t argument_0, generic64_t argument_1, generic64_t argument_2) {
    struct _PACKED struct_71 {
        uint8_t padding_at_0[4];
        generic32_t offset_4;
        generic32_t offset_8;
        generic32_t offset_12;
        uint8_t padding_at_16[8];
    } _stack;
    uint64_t _loop_state_var;
    int32_t _var_0;
    _stack.offset_12 = (number32_t) argument_0;
    _stack.offset_8 = (number32_t) argument_1;
    _stack.offset_4 = (number32_t) argument_2;
    _var_0 = printf_((const int8_t *) "B1");
    if (!((int32_t) _stack.offset_8 > (int32_t) 99)) {
        while (true) {
            int32_t _var_1;
            _var_1 = printf_((const int8_t *) "B2");
            if (!((int32_t) _stack.offset_12 > (int32_t) 19)) {
                while (true) {
                    int32_t _var_2;
                    _var_2 = printf_((const int8_t *) "B3");
                    if ((int32_t) _stack.offset_4 > (int32_t) 49) {
                        int32_t _var_3;
                        _var_3 = printf_((const int8_t *) "B4");
                        if (!((int32_t) _stack.offset_12 > (int32_t) 19)) {
                            continue;
                        }
                        break;
                    }
                    _loop_state_var = 1;
                    break;
                }
                if (_loop_state_var == 1) {
                    break;
                }
            }
            if (!((int32_t) _stack.offset_8 > (int32_t) 99)) {
                continue;
            }
            break;
        }
    }
    int32_t _var_4;
    _var_4 = printf_((const int8_t *) "B5");
}



_ABI(SystemV_x86_64)
generic64_t test_4(generic64_t argument_0, generic64_t argument_1) {
    struct _PACKED struct_72 {
        uint8_t padding_at_0[8];
        generic32_t offset_8;
        generic32_t offset_12;
        uint8_t padding_at_16[8];
    } _stack;
    int32_t _var_0;
    _stack.offset_12 = (number32_t) argument_0;
    _stack.offset_8 = (number32_t) argument_1;
    _var_0 = printf_((const int8_t *) "Block 1");
    while (true) {
        if (_stack.offset_12 == 1) {
            int32_t _var_1;
            _var_1 = printf_((const int8_t *) "Block 3");
            if ((int32_t) _stack.offset_8 > (int32_t) 4) {
                int32_t _var_2;
                _var_2 = printf_((const int8_t *) "Block 5");
                if (!((int32_t) _stack.offset_8 > (int32_t) 9)) {
                    continue;
                }
            } else {
                int32_t _var_3;
                _var_3 = printf_((const int8_t *) "Block 4");
            }
            int32_t _var_4;
            _var_4 = printf_((const int8_t *) "Block 6");
        } else {
            int32_t _var_5;
            _var_5 = printf_((const int8_t *) "Block 2");
            if ((int32_t) _stack.offset_8 > (int32_t) 19) {
                break;
            }
        }
    }
    int32_t _var_6;
    _var_6 = printf_((const int8_t *) "Block 7");
    return 0;
}
