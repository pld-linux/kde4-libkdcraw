Summary:	KDcraw libary
Summary(pl.UTF-8):	Biblioteka KDcraw
Name:		libkdcraw
Version:	0.1.4
Release:	2
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}.tar.bz2
# Source0-md5:	4fa5de407e9acf2eb5650d3fb5836f7d
Patch0:		kde-ac260-lt.patch
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDcraw Library is part of the KIPI Project.

%description -l pl.UTF-8
Biblioteka KDcraw jest częścią projektu KIPI.

%package devel
Summary:	Header files for libkdcraw development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających libkdcraw
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs-devel >= 9:3.2.0

%description devel
Header files for libkdcraw development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkdcraw.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdcraw.so.?.?.?
%attr(755,root,root) %ghost %{_libdir}/libkdcraw.so.?
%dir %{_libdir}/libkdcraw?
%attr(755,root,root) %{_libdir}/libkdcraw?/kdcraw
# is this needed by the program itself? dunno
%{_libdir}/libkdcraw?/CAMERALIST
%{_iconsdir}/hicolor/*x*/*/*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdcraw.so
%{_libdir}/libkdcraw.la
%{_includedir}/libkdcraw
%{_pkgconfigdir}/libkdcraw.pc
