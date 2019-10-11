colo molokai  
syntax on
set nu
set encoding=utf-8
set fileencodings=utf-8


set rtp+=~\vimfiles\bundle\vundle.vim
call vundle#begin('~/vimfiles/bundle')
" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

Plugin 'junegunn/goyo.vim'
Plugin 'junegunn/limelight.vim'
Plugin 'dhruvasagar/vim-table-mode'
Plugin 'dkarter/bullets.vim'
Plugin 'scrooloose/nerdtree' 
Plugin 'Xuyuanp/nerdtree-git-plugin' " NERDTree com git
Plugin 'tpope/vim-fugitive' " wrapper do git pra vim
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'kkoenig/wimproved.vim' " Uma melhor experiencia de Vim para o Windows fullscreen
Plugin 'iamcco/mathjax-support-for-mkdp'
Plugin 'tomasr/molokai'

" All of your Plugins must be added before the following line
"
call vundle#end()            " required
filetype plugin indent on    " required

let g:limelight_default_coefficient = 0.85
let g:table_mode_corner='|'

set autoindent       " Auto-indent new lines
set expandtab        " Use spaces instead of tabs
set shiftwidth=4     " Number of auto-indent spaces
set smartindent      " Enable smart-indent
set smarttab         " Enable smart-tabs
set softtabstop=4    " Number of spaces per Tab
set backspace=indent,eol,start  " Backspace behaviour
set linebreak
  
set directory^=$HOME/vimfiles/tmp//  
 
set ignorecase       " Busca inteligente
set incsearch        " Busca interativa
set hlsearch         " Marca todas as ocorrencias  

 
" Mapeamento
map <F2> :NERDTreeToggle <CR>
map <F6> :set spell spelllang=pt_br<CR>
map <C-o> :browse confirm e<cr>
map <F11> :Goyo 70%x95%<cr>
  
nnoremap <F11> :Goyo<cr>

" Start interactive EasyAlign in visual mode (e.g. vipga)
xmap ga <Plug>(EasyAlign)
" Start interactive EasyAlign for a motion/text object (e.g. gaip)
nmap ga <Plug>(EasyAlign)


let g:NERDTreeIndicatorMapCustom = {
    \ "Modified"  : "✹",
    \ "Staged"    : "✚",
    \ "Untracked" : "✭",
    \ "Renamed"   : "➜",
    \ "Unmerged"  : "═",
    \ "Deleted"   : "✖",
    \ "Dirty"     : "✗",
    \ "Clean"     : "✔︎",
    \ 'Ignored'   : '☒',
    \ "Unknown"   : "?"
    \ }
