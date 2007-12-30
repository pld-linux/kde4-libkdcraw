Summary:	KDcraw libary
Summary(pl.UTF-8):	Biblioteka KDcraw
Name:		libkdcraw
Version:	0.1.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}.tar.bz2
# Source0-md5:	dc4772804c17d7eff4f913048b8e1c3c
Patch0:		kde-ac260-lt.patch
URL:		http://extragear.kde.org/apps/kipi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	lcms-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The KDcraw Library is part of the KIPI Project.

%description -l pl.UTF-8
Biblioteka KDcraw jest częścią projektu KIPI.

%package devel
Summary:	Header files for libkdcraw development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających libkdcraw
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
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
%attr(755,root,root) %{_libdir}/lib*.so.?.?.?
%dir %{_libdir}/libkdcraw2
%attr(755,root,root) %{_libdir}/libkdcraw2/kdcraw
%{_iconsdir}/hicolor/*x*/*/*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libkdcraw
%{_pkgconfigdir}/*.pc
