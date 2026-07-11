%global tl_name leadsheets
%global tl_revision 61504

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Typesetting leadsheets and songbooks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/leadsheets
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/leadsheets.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/leadsheets.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package offers support for typesetting simple leadsheets of
songs, i.e. song lyrics and the corresponding chords.

