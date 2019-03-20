#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_with	python3	# CPython 3.x module [broken: async is a keyword in python 3.5+]
%bcond_without	tests	# unit tests

%define 	module	async
Summary:	Async Framework
Summary(pl.UTF-8):	Szkielet Async do programowania asynchronicznego
Name:		python-%{module}
Version:	0.6.2
Release:	2
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://pypi.org/simple/async/
Source0:	https://files.pythonhosted.org/packages/source/a/async/%{module}-%{version}.tar.gz
# Source0-md5:	9b06b5997de2154f3bc0273f80bcef6b
URL:		https://github.com/gitpython-developers/async
%if %{with python}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%{?with_tests:BuildRequires:	python-nose}
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-devel < 1:3.5
BuildRequires:	python3-setuptools
%{?with_tests:BuildRequires:	python3-nose}
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Async is a framework to process interdependent tasks in a pool of
workers.

%description -l pl.UTF-8
Async to szkielet do przetwarzania niezależnych zadań przez pulę
workerów.

%package -n python3-%{module}
Summary:	Async Framework
Summary(pl.UTF-8):	Szkielet Async do programowania asynchronicznego
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
Async is a framework to process interdependent tasks in a pool of
workers.

%description -n python3-%{module} -l pl.UTF-8
Async to szkielet do przetwarzania niezależnych zadań przez pulę
workerów.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/async/test
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/async/test
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%dir %{py_sitescriptdir}/async
%{py_sitescriptdir}/async/*.py[co]
%{py_sitescriptdir}/async-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%dir %{py3_sitescriptdir}/async
%{py3_sitescriptdir}/async/*.py
%{py3_sitescriptdir}/async/__pycache__
%{py3_sitescriptdir}/async-%{version}-py*.egg-info
%endif
