Name:		texlive-bpolynomial
Version:	15878
Release:	2
Summary:	Drawing polynomial functions of up to order 3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/bpolynomial
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpolynomial.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpolynomial.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This MetaPost package helps plotting polynomial and root
functions up to order three. The package provides macros to
calculate Bezier curves exactly matching a given constant,
linear, quadratic or cubic polynomial, or square or cubic root
function. In addition, tangents on all functions and
derivatives of polynomials can be calculated.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/bpolynomial/bpolynomial.mp
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/CHANGES
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/README
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/TODO
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/bpolynomial.pdf
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/bpolynomial.tex
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/examples.mp

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
