eqs = dict()

def define_env(env):

    @env.macro
    def label(eq: str):
        eqs[eq] = len(eqs) + 1
        return f'\\label{{{eqs[eq]}}}\\tag{{{eqs[eq]}}}'

    @env.macro
    def eqref(eq: str):
        return f'\\eqref{{{eqs[eq]}}}'
