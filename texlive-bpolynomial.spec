Name:		texlive-bpolynomial
Version:	0.5
Release:	1
Summary:	Drawing polynomial functions of up to order 3
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/bpolynomial
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpolynomial.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bpolynomial.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This MetaPost package helps plotting polynomial and root
functions up to order three. The package provides macros to
calculate Bezier curves exactly matching a given constant,
linear, quadratic or cubic polynomial, or square or cubic root
function. In addition, tangents on all functions and
derivatives of polynomials can be calculated.

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
%{_texmfdistdir}/metapost/bpolynomial/bpolynomial.mp
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/CHANGES
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/README
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/TODO
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/bpolynomial.pdf
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/bpolynomial.tex
%doc %{_texmfdistdir}/doc/metapost/bpolynomial/examples.mp

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
