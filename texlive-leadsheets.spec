Name:		texlive-leadsheets
Version:	61504
Release:	1
Summary:	Typesetting leadsheets and songbooks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leadsheets
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leadsheets.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leadsheets.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package offers support for typesetting simple
leadsheets of songs, i.e. song lyrics and the corresponding
chords.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/leadsheets
%doc %{_texmfdistdir}/doc/latex/leadsheets

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
