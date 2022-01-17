#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : anyio
Version  : 3.5.0
Release  : 20
URL      : https://files.pythonhosted.org/packages/4f/d0/b957c0679a9bd0ed334e2e584102f077c3e703f83d099464c3d9569b7c8a/anyio-3.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4f/d0/b957c0679a9bd0ed334e2e584102f077c3e703f83d099464c3d9569b7c8a/anyio-3.5.0.tar.gz
Summary  : High level compatibility layer for multiple asynchronous event loop implementations
Group    : Development/Tools
License  : MIT
Requires: anyio-license = %{version}-%{release}
Requires: anyio-python = %{version}-%{release}
Requires: anyio-python3 = %{version}-%{release}
BuildRequires : async_generator
BuildRequires : buildreq-distutils3
BuildRequires : curio
BuildRequires : pypi(contextvars)
BuildRequires : pypi(dataclasses)
BuildRequires : pypi(idna)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(sniffio)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://github.com/agronholm/anyio/actions/workflows/test.yml/badge.svg
:target: https://github.com/agronholm/anyio/actions/workflows/test.yml
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
Requires: pypi(contextvars)
Requires: pypi(dataclasses)
Requires: pypi(idna)
Requires: pypi(sniffio)
Requires: pypi(typing_extensions)

%description python3
python3 components for the anyio package.


%prep
%setup -q -n anyio-3.5.0
cd %{_builddir}/anyio-3.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642462759
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/anyio
cp %{_builddir}/anyio-3.5.0/LICENSE %{buildroot}/usr/share/package-licenses/anyio/097cca9910ea400331f4eed7d585982b04223e36
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
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
