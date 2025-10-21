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

    @env.macro
    def t(left: str, right: str) -> str:
        return f"<div style='display: flex; width: 100%;'><div style='float: left; width: 50%; text-align: center;'>{left}</div><div style='float: right; width: 50%; text-align: left;'>{right}</div></div>"

