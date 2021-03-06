#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : anyio
Version  : 2.2.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/d3/e6/901a94731af20e7109415525666cb3753a2bd1edd19616c2730448dffd0d/anyio-2.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d3/e6/901a94731af20e7109415525666cb3753a2bd1edd19616c2730448dffd0d/anyio-2.2.0.tar.gz
Summary  : High level compatibility layer for multiple asynchronous event loop implementations
Group    : Development/Tools
License  : MIT
Requires: anyio-license = %{version}-%{release}
Requires: anyio-python = %{version}-%{release}
Requires: anyio-python3 = %{version}-%{release}
Requires: async_generator
Requires: curio
Requires: dataclasses
Requires: idna
Requires: sniffio
Requires: typing_extensions
BuildRequires : async_generator
BuildRequires : buildreq-distutils3
BuildRequires : curio
BuildRequires : dataclasses
BuildRequires : idna
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : sniffio
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://github.com/agronholm/anyio/workflows/Python%20codeqa/test/badge.svg?branch=master
:target: https://github.com/agronholm/anyio/actions?query=workflow%3A%22Python+codeqa%2Ftest%22+branch%3Amaster
:alt: Build Status
.. image:: https://coveralls.io/repos/github/agronholm/anyio/badge.svg?branch=master
:target: https://coveralls.io/github/agronholm/anyio?branch=master
:alt: Code Coverage
.. image:: https://readthedocs.org/projects/anyio/badge/?version=latest
:target: https://anyio.readthedocs.io/en/latest/?badge=latest
:alt: Documentation
.. image:: https://badges.gitter.im/gitterHQ/gitter.svg
:target: https://gitter.im/python-trio/AnyIO
:alt: Gitter chat

%package license
Summary: license components for the anyio package.
Group: Default

%description license
license components for the anyio package.


%package python
Summary: python components for the anyio package.
Group: Default
Requires: anyio-python3 = %{version}-%{release}

%description python
python components for the anyio package.


%package python3
Summary: python3 components for the anyio package.
Group: Default
Requires: python3-core
Provides: pypi(anyio)
Requires: pypi(idna)
Requires: pypi(sniffio)

%description python3
python3 components for the anyio package.


%prep
%setup -q -n anyio-2.2.0
cd %{_builddir}/anyio-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1614609179
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/anyio
cp %{_builddir}/anyio-2.2.0/LICENSE %{buildroot}/usr/share/package-licenses/anyio/097cca9910ea400331f4eed7d585982b04223e36
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/anyio/097cca9910ea400331f4eed7d585982b04223e36

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
