%% Start of the file 'bristol.cls'.
%% Copyright 2021 Nicolas LESQUOY ('nicolas.lesquoy@gmail.com').
%
% This work may be distributed and/or modified under the
% conditions of the LaTeX Project Public License version 1.3c,
% available at http://www.latex-project.org/lppl/.
% #################################################
% IDENTIFICATION
% #################################################
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{bristol}[2021/12/29 v1 cheatsheet class]
% #################################################
% CLASS CONSTRUCTION
% #################################################
\LoadClassWithOptions{article} % The bristol class is based upon the original 'article class'
% Option declaration :
\DeclareOption{10pt}{\def\@@ptsize{10pt}}
\DeclareOption{11pt}{\def\@@ptsize{11pt}}
\DeclareOption{12pt}{\def\@@ptsize{12pt}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
% -------------------------------------------------
% LOADING NEEDED PACKAGES :
% -------------------------------------------------
% MATH :
\RequirePackage{amsthm}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{mathrsfs}
\RequirePackage{mathtools}
% LAYOUT:
\RequirePackage{enumitem}
\RequirePackage{hyperref} % For hyperlinks inside the document
\RequirePackage{tikz}
\RequirePackage[most]{tcolorbox} % For better boxes
\RequirePackage{xcolor}
\RequirePackage{pagecolor}
\RequirePackage{tocloft} % to modify the standard TOC
\RequirePackage[object=vectorian]{pgfornament} % For ornaments used on the titlepage
\RequirePackage{fancyhdr}
% FONT:
\RequirePackage{fontawesome} % For dingbats
\RequirePackage{adforn} % For more dingbats
% GEOMETRY SETTINGS:
\RequirePackage[paperheight=21cm,paperwidth=14.85cm,textheight=16cm,textwidth=13.85cm,inner=0.5cm,outer=0.5cm,top=2cm,twoside]{geometry}
% -------------------------------------------------
% COMMMAND DECLARATION :
% -------------------------------------------------
%% ID:
\newcounter{IDBox} % Counter for all environnements using \IDthm as identifier
\newcommand{\IDthm}[1]{\setlength{\fboxrule}{1pt}
\fcolorbox{black}{yellow}{\textsl{\texttt{#1:\thesection-\theIDBox}\stepcounter{IDBox}}}
}
\newcounter{myeq} % For the equation env.
\setcounter{myeq}{1}
%% AMSMATH ENV.:
\theoremstyle{plain}
\newtheorem{theorem}{Théorème}
\newtheorem{definition}{Définition}
\newtheorem{method}{Méthode}

\theoremstyle{definition}
\newtheorem{proposition}{Proposition}
\newtheorem{corollary}{Corollaire}

\theoremstyle{remark}
\newtheorem{lemma}{Lemme}
\newtheorem{example}{Exemple}
\newtheorem{exercise}{Exercice}
\newtheorem{remark}{Remarque}
%% TCB BOXES DEF:
\newtcolorbox{equationbox}[1]{colback=orange!5!white,colframe=orange!75,
title=\'Equation \thesection(\romannumeral\themyeq) $\blacktriangleright$ {#1}\stepcounter{myeq},enhanced}
\newtcolorbox{theorembox}{colback=red!20,colframe=red!50,breakable}
\newtcolorbox{definitionbox}{colback=green!20,colframe=green!50,breakable}
\newtcolorbox{propositionbox}{colback=violet!20,colframe=violet!50,breakable}
\newtcolorbox{lemmabox}{colback=cyan!20,colframe=cyan!50,breakable}
\newtcolorbox{corollarybox}{colback=blue!20,colframe=blue!50,breakable}
\newtcolorbox{methodebox}{colback=teal!20,colframe=teal!50,breakable}
%% CORRESPONDING BOXES:
\newenvironment{thmbox}[1]{
    \begin{theorembox}
    	\begin{theorem}[#1]\hspace{1pt}\faChevronRight\hspace{1pt}\IDthm{thm}\\}
{
    	\end{theorem}
    \end{theorembox}
}
\newenvironment{defbox}[1]{
    \begin{definitionbox}
    	\begin{definition}[#1]\hspace{1pt}\faChevronRight\hspace{1pt}\IDthm{def}\\}
{
    	\end{definition}
    \end{definitionbox}
}
\newenvironment{prpbox}[1]{
    \begin{propositionbox}
    	\begin{proposition}[#1]\hspace{1pt}\faChevronRight\hspace{1pt}\IDthm{prp}\\}
{
    	\end{proposition}
    \end{propositionbox}
}
\newenvironment{lembox}[1]{
    \begin{lemmabox}
    	\begin{lemma}[#1]\hspace{1pt}\faChevronRight\hspace{1pt}\IDthm{lem}\\}
{
    	\end{lemma}
    \end{lemmabox}
}
\newenvironment{corbox}[1]{
    \begin{corollarybox}
    	\begin{corollary}[#1]\hspace{1pt}\faChevronRight\hspace{1pt}\IDthm{cor}\\}
{
    	\end{corollary}
    \end{corollarybox}
}
\newenvironment{mtdbox}[1]{
    \begin{methodebox}
    	\begin{methode}[#1]\hspace{1pt}\faChevronRight\hspace{1pt}\IDthm{cor}\\}
{
    	\end{methode}
    \end{methodebox}
}
\newcommand{\newequation}[3]{
	\begin{tcolorbox}[colback=orange!5!white,colframe=orange!75,
	title=\'Equation \thesection(\romannumeral\themyeq) $\blacktriangleright$ {#1}\stepcounter{myeq},enhanced]
		#2
	\tcblower
		{\renewcommand\labelitemi{\faCheckSquareO}
		#3} % #3 is intented to be a list.
	\end{tcolorbox}
}

%% TITLEPAGE:
\newcommand{\thisornament}[1][68]{\pgfornament[width=0.5\textwidth]{#1}} % Producing the ornament
\newcommand{\myTitlepage}[5]
  {%
    \newpagecolor{#5}% Changing page color
    \newgeometry{top=2cm,left=1cm,right=1cm,bottom=0.5cm}%
    \begin{titlepage}%
      \centering
      \large
      #4 -- \today\par
      % Title
      \vspace{2cm}%
      \begingroup
        \Huge
        \sbox0{#1}%
        \ifdim\wd0>\linewidth
          \unhbox0
        \else
          \resizebox{\linewidth}{!}{\usebox0}%
        \fi
        \par
      \endgroup
      \vspace{0.5cm}
      \large \adforn{32}\quad#2\quad\adforn{60}\par
      \vspace{0.5cm}%
      \thisornament\par
      \vspace{1cm}%
      \begin{tcolorbox}
        [
           breakable
          ,enhanced
          ,title=\contentsname
          ,colframe=black
          ,colback=white
          ,colbacktitle=white
          ,fonttitle=\bfseries
          ,coltitle=black
          ,attach boxed title to top center=
            {%
               yshift=-0.25mm-\tcboxedtitleheight/2
              ,yshifttext=2mm-\tcboxedtitleheight/2
            }
          ,boxed title style=
            {%
               boxrule=0.5mm
              ,frame code=
                {%
                  \path[tcb fill frame] ([xshift=-4mm]frame.west)
                  -- (frame.north west) -- (frame.north east)
                  -- ([xshift=4mm]frame.east) -- (frame.south east)
                  -- (frame.south west) -- cycle;%
                }
              ,interior code=
                {%
                  \path[tcb fill interior] ([xshift=-2mm]interior.west)
                  -- (interior.north west) -- (interior.north east)
                  -- ([xshift=2mm]interior.east) -- (interior.south east)
                  -- (interior.south west) -- cycle;%
                }%
            }%
        ]%
        % TOC display
        \@starttoc{toc}%
      \end{tcolorbox}%
      \vfill
    \end{titlepage}%
    ~\newpage
    \restorepagecolor
    \restoregeometry
  }
\makeatother

%% FANCYHDR COMMANDS:
\pagestyle{fancy}
% % No HEADER
\fancyhead[L]{} 
\fancyhead[R]{}
\fancyhead[C]{}
\renewcommand\headrulewidth{0pt}
\fancyfoot[L]{Titre}
\fancyfoot[R]{\adforn{64}\;\textbf{\thepage}}
\fancyfoot[C]{} % Deletes centered page numbers
%% TOCLOFT COMMANDS:
% To have dotted lines in TOC
%\renewcommand\cftsecfont{\normalfont}
%\renewcommand\cftsecpagefont{\normalfont}
\renewcommand{\cftsecleader}{\cftdotfill{\cftsecdotsep}}
\renewcommand\cftsecdotsep{\cftdot}
\renewcommand\cftsubsecdotsep{\cftdot}

%% BUTTONS:
% Script copied from 'https://tex.stackexchange.com/questions/628406/beamer-buttons-in-article'

% copied from beamercolorthemedefault.sty
% begin
\definecolor{buttoncolor}{rgb}{0.2,0.2,0.7}
% end

\colorlet{button}{buttoncolor}
\colorlet{button border}{buttoncolor}

\makeatletter
\newbox\beamer@tempbox
\newdimen\beamer@tempdim

% copied from beamerinnerthemedefault.sty
% begin
\newdimen\beamer@dima
\newdimen\beamer@dimb

%\defbeamertemplate*{button}{default}
\def\beamer@@tmpl@button
{%
	\setbox\beamer@tempbox=\hbox{{\insertbuttontext}}%
	\ht\beamer@tempbox=6pt%
	\dp\beamer@tempbox=0pt%
	\setbox\beamer@tempbox=\vbox{\box\beamer@tempbox\vskip2pt}%
	\beamer@tempdim=\wd\beamer@tempbox%
	\beamer@dima=\beamer@tempdim\advance\beamer@dima by2.2pt
	\beamer@dimb=\beamer@tempdim\advance\beamer@dimb by4pt
	\begin{pgfpicture}{-4pt}{0pt}{\the\beamer@tempdim}{8pt}
	%    \color{bg}
	    \pgfsetfillcolor{button}
	    \pgfsetlinewidth{0.8pt}
	    \pgfpathqmoveto{0pt}{0pt}
	    \pgfpathqcurveto{-2.2pt}{0pt}{-4pt}{1.8pt}{-4pt}{4pt}
	    \pgfpathqcurveto{-4pt}{6.2pt}{-2.2pt}{8pt}{0pt}{8pt}
	    \pgfpathlineto{\pgfpoint{\the\beamer@tempdim}{8pt}}
	    \pgfpathcurveto%
	    {\pgfpoint{\the\beamer@dima}{8pt}}%
	    {\pgfpoint{\the\beamer@dimb}{6.2pt}}%
	    {\pgfpoint{\the\beamer@dimb}{4pt}}
	    \pgfpathcurveto%
	    {\pgfpoint{\the\beamer@dimb}{1.8pt}}%
	    {\pgfpoint{\the\beamer@dima}{0pt}}%
	    {\pgfpoint{\the\beamer@tempdim}{0pt}}
	    \pgfpathclose
	    \pgfusepathqfill
		%\colorlet{bg}{parent.bg}
		%\usebeamercolor[fg]{button border}
	    \pgfsetstrokecolor{button border}
	    \pgfpathqmoveto{0pt}{0pt}
	    \pgfpathqcurveto{-2.2pt}{0pt}{-4pt}{1.8pt}{-4pt}{4pt}
	    \pgfpathqcurveto{-4pt}{6.2pt}{-2.2pt}{8pt}{0pt}{8pt}
	    \pgfpathlineto{\pgfpoint{\the\beamer@tempdim}{8pt}}
	    \pgfpathcurveto%
	    {\pgfpoint{\the\beamer@dima}{8pt}}%
	    {\pgfpoint{\the\beamer@dimb}{6.2pt}}%
	    {\pgfpoint{\the\beamer@dimb}{4pt}}
	    \pgfpathcurveto%
	    {\pgfpoint{\the\beamer@dimb}{1.8pt}}%
	    {\pgfpoint{\the\beamer@dima}{0pt}}%
	    {\pgfpoint{\the\beamer@tempdim}{0pt}}
	    \pgfpathclose
	    \pgfusepathqstroke
    \end{pgfpicture}%
    \hskip-\beamer@tempdim%
    \box\beamer@tempbox%
    \kern4pt%
}
% end

% copied from beamerbasenavigation.sty
% begin
\pgfdefobject{beamergotosymbol}{\pgfpoint{0pt}{-1pt}}{\pgfpoint{5pt}{5pt}}
{
    \pgfpathqmoveto{1.5bp}{0.5bp}
    \pgfpathqlineto{3.5bp}{2bp}
    \pgfpathqlineto{1.5bp}{3.5bp}
    \pgfusepathqfill
}

\def\insertgotosymbol{%
    \begin{pgfpicture}{1pt}{0pt}{6pt}{5pt}
    	\pgfuseobject{beamergotosymbol}%
    \end{pgfpicture}}

	\pgfdefobject{beamerskipsymbol}{\pgfpoint{0pt}{-1pt}}{\pgfpoint{7pt}{5pt}}
	{
	    \pgfpathqmoveto{1.5bp}{0.5bp}
	    \pgfpathqlineto{3.5bp}{2bp}
	    \pgfpathqlineto{1.5bp}{3.5bp}
	    \pgfpathqmoveto{3.5bp}{0.5bp}
	    \pgfpathqlineto{5.5bp}{2bp}
	    \pgfpathqlineto{3.5bp}{3.5bp}
	    \pgfusepathqfill
}

\def\insertskipsymbol{%
    \begin{pgfpicture}{1pt}{0pt}{8pt}{5pt}
    	\pgfuseobject{beamerskipsymbol}%
    \end{pgfpicture}}


	\pgfdefobject{beamerreturnsymbol}{\pgfpoint{0pt}{-1pt}}{\pgfpoint{5pt}{5pt}}
	{
	    \pgfpathqmoveto{3.5bp}{0.5bp}
	    \pgfpathqlineto{1.5bp}{2bp}
	    \pgfpathqlineto{3.5bp}{3.5bp}
	    \pgfusepathqfill
}

\def\insertreturnsymbol{%
    \begin{pgfpicture}{1pt}{0pt}{6pt}{5pt}
    	\pgfuseobject{beamerreturnsymbol}%
    \end{pgfpicture}}


%\def\beamerbutton#1{\def\insertbuttontext{#1}\usebeamertemplate**{button}}
\def\beamerbutton#1{%
    \def\insertbuttontext{#1}%
    {\sffamily\tiny\color{white}\beamer@@tmpl@button}}
\def\beamergotobutton#1{\beamerbutton{\insertgotosymbol#1}}
\def\beamerskipbutton#1{\beamerbutton{\insertskipsymbol#1}}
\def\beamerreturnbutton#1{\beamerbutton{\insertreturnsymbol#1}}
% end
\makeatother

\newcommand{\myhyperlink}[2]{%
    {\hypersetup{hidelinks}\hyperlink{#1}{#2}}}

%% PUNCHHOLES:
\AddToHook{shipout/background}{%
	\begin{tikzpicture}[overlay,remember picture,every node/.style={circle, minimum height=5mm,minimum width=5mm,draw}]
	\draw (current page.north) node[yshift=-10mm,xshift = 40mm]{};
	\draw (current page.north) node[yshift=-10mm,xshift= -40mm]{};
	\end{tikzpicture}%
}
% end of the file