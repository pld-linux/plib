Summary:	Portable Game Library
Summary(pl):	Przenaszalna Biblioteka do programowania Gier
Name:		plib
Version:	1.7.0
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://plib.sourceforge.net/dist/%{name}-%{version}.tar.gz
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


%description
Portable Game Library.

%description -l pl
Przenaszalna Biblioteka do programowania Gier.

%prep
%setup -q

%build
rm -f config.cache missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-GL=%{_prefix}

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README* NOTICE NEWS ChangeLog
%{_includedir}/plib
%{_libdir}/lib*.a
