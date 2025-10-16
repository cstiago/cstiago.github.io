def define_env(env):

    @env.macro
    def label(eq):
        return f'\\label{{{eq}}}\\tag{{{eq}}}'

    @env.macro
    def eqref(eq):
        return f'\\eqref{{{eq}}}'
