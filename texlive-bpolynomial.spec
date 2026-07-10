%global tl_name bpolynomial
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.5
Release:	%{tl_revision}.1
Summary:	Drawing polynomial functions of up to order 3
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/bpolynomial
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bpolynomial.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bpolynomial.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This MetaPost package helps plotting polynomial and root functions up to
order three. The package provides macros to calculate Bezier curves
exactly matching a given constant, linear, quadratic or cubic
polynomial, or square or cubic root function. In addition, tangents on
all functions and derivatives of polynomials can be calculated.

