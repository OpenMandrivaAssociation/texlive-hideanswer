Name:		texlive-hideanswer
Version:	63852
Release:	2
Summary:	Generate documents with and without answers by toggling a switch
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hideanswer
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hideanswer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hideanswer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package can generate documents with and without answers
from a single file by toggling a switch. However, it can only
be used to create documents to be printed on paper.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hideanswer
%doc %{_texmfdistdir}/doc/latex/hideanswer

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
