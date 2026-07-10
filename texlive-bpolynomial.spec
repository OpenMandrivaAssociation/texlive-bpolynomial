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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This MetaPost package helps plotting polynomial and root functions up to
order three. The package provides macros to calculate Bezier curves
exactly matching a given constant, linear, quadratic or cubic
polynomial, or square or cubic root function. In addition, tangents on
all functions and derivatives of polynomials can be calculated.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/metapost
%dir %{_datadir}/texmf-dist/doc/metapost
%dir %{_datadir}/texmf-dist/metapost/bpolynomial
%dir %{_datadir}/texmf-dist/doc/metapost/bpolynomial
%doc %{_datadir}/texmf-dist/doc/metapost/bpolynomial/CHANGES
%doc %{_datadir}/texmf-dist/doc/metapost/bpolynomial/README
%doc %{_datadir}/texmf-dist/doc/metapost/bpolynomial/TODO
%doc %{_datadir}/texmf-dist/doc/metapost/bpolynomial/bpolynomial.pdf
%doc %{_datadir}/texmf-dist/doc/metapost/bpolynomial/bpolynomial.tex
%doc %{_datadir}/texmf-dist/doc/metapost/bpolynomial/examples.mp
%{_datadir}/texmf-dist/metapost/bpolynomial/bpolynomial.mp
