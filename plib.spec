Summary:	plib
Summary(pl):	plib
Name:		plib
Version:	1.3.1
Release:	1
License:	LGPL
Group:		Libraries
Source:		http://plib.sourceforge.net/dist/%name-%version.tar.gz
Patch:		plib_configure.in_ssgAux_add.patch
BuildRequires:	XFree86-devel >= 4.0.1
BuildRequires:	OpenGL-devel
BuildRequires:	glut-devel >= 3.7
Requires:	OpenGL
Buildroot:	/tmp/%{name}-%{version}-root

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define	_prefix	/usr/X11R6

%description

%description -l pl

%prep
%setup -q

%patch -p0

%build
autoconf
rm -f config.cache
%configure --prefix=%{_prefix} \
	--with-gl=%{_prefix} \
	--with-x 

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 

bzip2 -9 AUTHORS README* NOTICE NEWS ChangeLog CHANGES

%install
rm -rf  $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

#cd $RPM_BUILD_ROOT/usr/X11R6/include
#mkdir plib
#mv *.h plib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.bz2 README*.bz2 NOTICE.bz2 NEWS.bz2 ChangeLog.bz2 CHANGES.bz2
%attr(644,root,root) %{_includedir}/plib/*.h

%attr(644,root,root) %{_libdir}/libplib*.a
