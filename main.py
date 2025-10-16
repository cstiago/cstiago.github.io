eqs = {}

def handle_eq(eq: str) -> int:
    if eq not in eqs:
        eqs[eq] = len(eqs) + 1
    return eqs[eq]

def define_env(env):

    @env.macro
    def label(eq: str):
        ref = handle_eq(eq)
        return f'\\label{{{ref}}}\\tag{{{ref}}}'

    @env.macro
    def eqref(eq: str):
        ref = handle_eq(eq)
        return f'\\eqref{{{ref}}}'
