Summary:	Portable game library
Summary(pl):	Przeno¶na biblioteka do programowania gier
Name:		plib
Version:	1.8.3
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://plib.sourceforge.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	de10b19dfcee5da7115ee2a69656f34c
Patch0:		%{name}-shared.patch
URL:		http://plib.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 4.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
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
Requires:	OpenGL-devel-base

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

%build
rm -f config.cache missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-GL=/usr/X11R6

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
