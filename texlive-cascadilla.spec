%global tl_name cascadilla
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8.2
Release:	%{tl_revision}.1
Summary:	Typeset papers conforming to the stylesheet of the Cascadilla Proceedings Pro...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cascadilla
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadilla.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadilla.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class provides an extension of the standard LaTeX article class that
may be used to typeset papers conforming to the stylesheet of the
Cascadilla Proceedings Project, which is used by a number of linguistics
conference proceedings (e.g., WCCFL).

