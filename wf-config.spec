#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	A library for managing configuration files, written for wayfire
Summary(pl.UTF-8):	Napisana dla wayfire biblioteka do zarządzania plikami konfiguracyjnymi
Name:		wf-config
Version:	0.8.0
Release:	3
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/WayfireWM/wf-config/releases
Source0:	https://github.com/WayfireWM/wf-config/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	633cd902c2c889ae02c6ffeef8b44357
URL:		https://wayfire.org/
BuildRequires:	GLM-devel >= 0.9.9.9
BuildRequires:	libevdev-devel
BuildRequires:	libstdc++-devel >= 6:9
BuildRequires:	libxml2-devel
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library for managing configuration files, written for wayfire.

%description -l pl.UTF-8
Napisana dla wayfire biblioteka do zarządzania plikami
konfiguracyjnymi.

%package devel
Summary:	Header files for wf-config library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wf-config
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	GLM-devel >= 0.9.9.9
Requires:	libevdev-devel
Requires:	libstdc++-devel >= 6:9
Requires:	libxml2-devel

%description devel
Header files for wf-config library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wf-config.

%package static
Summary:	Static wf-config library
Summary(pl.UTF-8):	Biblioteka statyczna wf-config
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static wf-config library.

%description static -l pl.UTF-8
Biblioteka statyczna wf-config.

%prep
%setup -q

%build
%meson build \
	%{!?with_static_libs:--default-library=shared}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwf-config.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwf-config.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwf-config.so
%{_includedir}/wayfire/config
%{_includedir}/wayfire/util
%{_pkgconfigdir}/wf-config.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libwf-config.a
%endif
