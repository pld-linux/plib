Summary:	Portable Game Library
Summary(pl):	Przenaszalna Biblioteka do programowania Gier
Name:		plib
Version:	1.3.1
Release:	1
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(pl):	X11/Biblioteki
Source0:	http://plib.sourceforge.net/dist/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-flt-max.patch
URL:		http://plib.sourceforge.net/
BuildRequires:	XFree86-devel >= 4.0.1
BuildRequires:	OpenGL-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	glut-devel >= 3.7
BuildRequires:	libstdc++-devel
Requires:	OpenGL
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Portable Game Library.

%description -l pl
Przenaszalna Biblioteka do programowania Gier.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f config.cache missing
aclocal
autoconf
automake -a -c
%configure \
	--with-gl=%{_prefix}

%{__make}

gzip -9nf AUTHORS README* NOTICE NEWS ChangeLog CHANGES

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_includedir}/plib
%{_libdir}/lib*.a
