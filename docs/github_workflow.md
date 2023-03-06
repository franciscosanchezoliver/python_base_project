## Trigger branches
> on:\
>   push:\
>     branches:    \
>       - '*'         # matches every branch that doesn't contain a '/'\
>       - '*/*'       # matches every branch containing a single '/'\
>       - '**'        # matches every branch\
>       - '!master'   # excludes master

