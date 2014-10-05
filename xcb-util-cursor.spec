Summary:	XCB util-cursor module
Name:		xcb-util-cursor
Version:	0.1.1
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://xcb.freedesktop.org/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	568712eaa340f18b357d3748300c1795
URL:		http://xcb.freedesktop.org/XcbCursor/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gperf
BuildRequires:	libtool
BuildRequires:	m4
BuildRequires:	pkg-config
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-renderutil-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XCB util-cursor module provides the following libraries:
- cursor: port of libxcursor

%package devel
Summary:	Header files for XCB util-cursor library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for XCB util-image library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libxcb-cursor.so.?
%attr(755,root,root) %{_libdir}/libxcb-cursor.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxcb-cursor.so
%{_includedir}/xcb/*.h
%{_pkgconfigdir}/*.pc

