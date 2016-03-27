#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module [functionality already in 3.4+]

Summary:	Backport of functools.singledispatch from Python 3.4 to Python 2.6-3.3
Summary(pl.UTF-8):	Backport functools.singledispatch z Pythona 3.4 do Pythona 2.6-3.3
Name:		python-singledispatch
Version:	3.4.0.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/singledispatch
Source0:	https://pypi.python.org/packages/source/s/singledispatch/singledispatch-%{version}.tar.gz
# Source0-md5:	af2fc6a3d6cc5a02d0bf54d909785fcb
URL:		https://pypi.python.org/pypi/singledispatch
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-modules < 1:3.4
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
Requires:	python-six
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PEP 443 (<http://www.python.org/dev/peps/pep-0443/>) proposed to
expose a mechanism in the functools standard library module in Python 3.4
that provides a simple form of generic programming known as
single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

%description -l pl.UTF-8
PEP 443 (<http://www.python.org/dev/peps/pep-0443/>) zaproponował
udostępnienie mechanizmu w module biblioteki standardowej functools w
Pythonie 3.4 udostępniającą prostą postać programowania generycznego,
znaną jako funkcje generyczne single-dispatch.

Ten moduł to backport tej funkcji do Pythona w wersjach 2.6 - 3.3.

%package -n python3-singledispatch
Summary:	Backport of functools.singledispatch from Python 3.4 to Python 2.6-3.3
Summary(pl.UTF-8):	Backport functools.singledispatch z Pythona 3.4 do Pythona 2.6-3.3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2
Requires:	python3-modules < 1:3.4
Requires:	python3-six

%description -n python3-singledispatch
PEP 443 (<http://www.python.org/dev/peps/pep-0443/>) proposed to
expose a mechanism in the functools standard library module in Python 3.4
that provides a simple form of generic programming known as
single-dispatch generic functions.

This library is a backport of this functionality to Python 2.6 - 3.3.

%description -n python3-singledispatch -l pl.UTF-8
PEP 443 (<http://www.python.org/dev/peps/pep-0443/>) zaproponował
udostępnienie mechanizmu w module biblioteki standardowej functools w
Pythonie 3.4 udostępniającą prostą postać programowania generycznego,
znaną jako funkcje generyczne single-dispatch.

Ten moduł to backport tej funkcji do Pythona w wersjach 2.6 - 3.3.

%prep
%setup -q -n singledispatch-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/singledispatch.py[co]
%{py_sitescriptdir}/singledispatch_helpers.py[co]
%{py_sitescriptdir}/singledispatch-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-singledispatch
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/singledispatch.py
%{py3_sitescriptdir}/singledispatch_helpers.py
%{py3_sitescriptdir}/__pycache__/singledispatch.cpython-*.py[co]
%{py3_sitescriptdir}/__pycache__/singledispatch_helpers.cpython-*.py[co]
%{py3_sitescriptdir}/singledispatch-%{version}-py*.egg-info
%endif
