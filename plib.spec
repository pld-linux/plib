Summary:	Portable game library
Summary(pl):	Przenośna biblioteka do programowania gier
Name:		plib
Version:	1.7.0
Release:	4
License:	LGPL
Group:		X11/Libraries
Source0:	http://plib.sourceforge.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	30881640e37bf650e203e10a23f879c7
Patch0:		%{name}-shared.patch
URL:		http://plib.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 4.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glut-devel >= 3.7
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Portable game library.

%description -l pl
Przenośna biblioteka do programowania gier.

%package devel
Summary:	Header files for plib library
Summary(pl):	Pliki nagłówkowe biblioteki plib
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL-devel-base

%description devel
Header files for plib library.

%description devel -l pl
Pliki nagłówkowe biblioteki plib.

%package static
Summary:	Static plib libraries
Summary(pl):	Statyczne biblioteki plib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

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
