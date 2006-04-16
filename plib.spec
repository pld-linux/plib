Summary:	Portable game library
Summary(pl):	Przeno¶na biblioteka do programowania gier
Name:		plib
Version:	1.8.4
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://plib.sourceforge.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	5e3f289a9d1c5de0b1cfdec76bf139e6
Patch0:		%{name}-shared.patch
Patch1:		%{name}-js_fix.patch
Patch2:		%{name}-gcc4.patch
URL:		http://plib.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXmu-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Portable game library.

%description -l pl
Przeno¶na biblioteka do programowania gier.

%package devel
Summary:	Header files for plib library
Summary(pl):	Pliki nag³ówkowe biblioteki plib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel
Requires:	libstdc++-devel
Requires:	xorg-lib-libXi-devel
Requires:	xorg-lib-libXmu-devel

%description devel
Header files for plib library.

%description devel -l pl
Pliki nag³ówkowe biblioteki plib.

%package static
Summary:	Static plib libraries
Summary(pl):	Statyczne biblioteki plib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static plib libraries.

%description static -l pl
Statyczne biblioteki plib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f config.cache missing
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
