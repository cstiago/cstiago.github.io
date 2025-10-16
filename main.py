eqs = {}

def handle_eq(eq: str, comp: str='') -> str:
    ref = str()
    if eq not in eqs:
        eqs[eq] = len(eqs) + 1
        ref = str(eqs[eq])
    if comp:
        ref += comp
    return ref

def define_env(env):

    @env.macro
    def label(eq: str, comp: str='') -> str:
        ref = handle_eq(eq, comp)
        return f'\\label{{{ref}}}\\tag{{{ref}}}'

    @env.macro
    def eqref(eq: str, comp: str='') -> str:
        ref = handle_eq(eq, comp)
        return f'\\eqref{{{ref}}}'
