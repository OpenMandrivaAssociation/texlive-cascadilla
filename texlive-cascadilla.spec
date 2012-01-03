# revision 24589
# category Package
# catalog-ctan /macros/latex/contrib/cascadilla
# catalog-date 2011-11-13 08:18:31 +0100
# catalog-license lppl
# catalog-version 1.8.1
Name:		texlive-cascadilla
Version:	1.8.1
Release:	2
Summary:	Typeset papers conforming to the stylesheet of the Cascadilla Proceedings Project
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cascadilla
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadilla.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cascadilla.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides an extension of the standard LaTeX article
class that may be used to typeset papers conforming to the
stylesheet of the Cascadilla Proceedings Project, which is used
by a number of linguistics conference proceedings (e.g.,
WCCFL).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
