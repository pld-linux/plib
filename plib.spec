Summary:	Portable Game Library
Summary(pl):	Przenaszalna Biblioteka do programowania Gier
Name:		plib
Version:	1.7.0
Release:	3
License:	LGPL
Group:		X11/Libraries
Source0:	http://plib.sourceforge.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	30881640e37bf650e203e10a23f879c7
URL:		http://plib.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel >= 4.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glut-devel >= 3.7
BuildRequires:	libstdc++-devel
Requires:	OpenGL
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Portable Game Library.

%description -l pl
Przenaszalna Biblioteka do programowania Gier.

%package devel
Summary:	Header files for plib library
Summary(pl):	Pliki nag³ówkowe biblioteki plib
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL-devel-base

%description devel
Header files for plib library.

%description devel -l pl
Pliki nag³ówkowe biblioteki plib.

%prep
%setup -q

%build
rm -f config.cache missing
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
%{_libdir}/lib*.a

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
