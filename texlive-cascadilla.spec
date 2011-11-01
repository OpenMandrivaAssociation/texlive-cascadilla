Name:		texlive-cascadilla
Version:	1.8
Release:	1
Summary:	A document class for typesetting papers conforming to the stylesheet of the Cascadilla Proceedings Project
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cascadilla
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadilla.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadilla.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The class provides an extension of the standard LaTeX article
class that may be used to typeset papers conforming to the
stylesheet of the Cascadilla Proceedings Project, which is used
by a number of linguistics conference proceedings (e.g.,
WCCFL).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/cascadilla/cascadilla.bst
%{_texmfdistdir}/tex/latex/cascadilla/cascadilla.cls
%doc %{_texmfdistdir}/doc/latex/cascadilla/LICENSE.txt
%doc %{_texmfdistdir}/doc/latex/cascadilla/README
%doc %{_texmfdistdir}/doc/latex/cascadilla/example.pdf
%doc %{_texmfdistdir}/doc/latex/cascadilla/example.tex
%doc %{_texmfdistdir}/doc/latex/cascadilla/exampleref.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
