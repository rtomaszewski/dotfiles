# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

export HISTSIZE=100000
export HISTFILESIZE=200000
# export EDITOR=vim

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

alias ls='ls --color=auto'
alias dir='dir --color=auto'

alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -al'
alias i='egrep'

alias o='less'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias cd..='cd ..'

alias myip='curl --silent checkip.dyndns.org | egrep --only-matching "[0-9\.]+"'
#alias ipython='ipython --colors Linux'
alias ipython='ipython  --colors Linux --autocall=2'


alias homeshick="source $HOME/.homesick/repos/homeshick/bin/homeshick.sh"

for i in $HOME/.bashrc_*; do 
  #echo $i; done
  . $i
done

