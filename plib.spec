Summary:	Portable game library
Summary(pl.UTF-8):	Przenośna biblioteka do programowania gier
Name:		plib
Version:	1.8.5
Release:	3
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://plib.sourceforge.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	47a6fbf63668c1eed631024038b2ea90
Patch0:		%{name}-shared.patch
Patch1:		%{name}-link.patch
URL:		https://plib.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1

%description
Portable game library.

%description -l pl.UTF-8
Przenośna biblioteka do programowania gier.

%package devel
Summary:	Header files for plib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki plib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel
Requires:	libstdc++-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXmu-devel

%description devel
Header files for plib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki plib.

%package static
Summary:	Static plib libraries
Summary(pl.UTF-8):	Statyczne biblioteki plib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static plib libraries.

%description static -l pl.UTF-8
Statyczne biblioteki plib.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README* NOTICE NEWS ChangeLog
%{_libdir}/libplibfnt.so.*.*.*
%ghost %{_libdir}/libplibfnt.so.0
%{_libdir}/libplibjs.so.*.*.*
%ghost %{_libdir}/libplibjs.so.0
%{_libdir}/libplibnet.so.*.*.*
%ghost %{_libdir}/libplibnet.so.0
%{_libdir}/libplibpsl.so.*.*.*
%ghost %{_libdir}/libplibpsl.so.0
%{_libdir}/libplibpu.so.*.*.*
%ghost %{_libdir}/libplibpu.so.0
%{_libdir}/libplibpuaux.so.*.*.*
%ghost %{_libdir}/libplibpuaux.so.0
%{_libdir}/libplibpw.so.*.*.*
%ghost %{_libdir}/libplibpw.so.0
%{_libdir}/libplibsg.so.*.*.*
%ghost %{_libdir}/libplibsg.so.0
%{_libdir}/libplibsl.so.*.*.*
%ghost %{_libdir}/libplibsl.so.0
%{_libdir}/libplibsm.so.*.*.*
%ghost %{_libdir}/libplibsm.so.0
%{_libdir}/libplibssg.so.*.*.*
%ghost %{_libdir}/libplibssg.so.0
%{_libdir}/libplibssgaux.so.*.*.*
%ghost %{_libdir}/libplibssgaux.so.0
%{_libdir}/libplibul.so.*.*.*
%ghost %{_libdir}/libplibul.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libplibfnt.so
%{_libdir}/libplibjs.so
%{_libdir}/libplibnet.so
%{_libdir}/libplibpsl.so
%{_libdir}/libplibpu.so
%{_libdir}/libplibpuaux.so
%{_libdir}/libplibpw.so
%{_libdir}/libplibsg.so
%{_libdir}/libplibsl.so
%{_libdir}/libplibsm.so
%{_libdir}/libplibssg.so
%{_libdir}/libplibssgaux.so
%{_libdir}/libplibul.so
%{_libdir}/libplibfnt.la
%{_libdir}/libplibjs.la
%{_libdir}/libplibnet.la
%{_libdir}/libplibpsl.la
%{_libdir}/libplibpu.la
%{_libdir}/libplibpuaux.la
%{_libdir}/libplibpw.la
%{_libdir}/libplibsg.la
%{_libdir}/libplibsl.la
%{_libdir}/libplibsm.la
%{_libdir}/libplibssg.la
%{_libdir}/libplibssgaux.la
%{_libdir}/libplibul.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libplibfnt.a
%{_libdir}/libplibjs.a
%{_libdir}/libplibnet.a
%{_libdir}/libplibpsl.a
%{_libdir}/libplibpu.a
%{_libdir}/libplibpuaux.a
%{_libdir}/libplibpw.a
%{_libdir}/libplibsg.a
%{_libdir}/libplibsl.a
%{_libdir}/libplibsm.a
%{_libdir}/libplibssg.a
%{_libdir}/libplibssgaux.a
%{_libdir}/libplibul.a
