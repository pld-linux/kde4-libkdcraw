%define         _state          stable
%define		orgname		libkdcraw
%define         qtver           4.7.4

Summary:	KDcraw libary
Summary(pl.UTF-8):	Biblioteka KDcraw
Name:		libkdcraw
Version:	4.7.3
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	ea57e7b64c235e5d5dd070cb7dca312e
URL:		http://www.kde.org/
BuildRequires:	lcms-devel
BuildRequires:	libjpeg-devel
BuildRequires:	rpmbuild(macros) >= 1.164
Obsoletes:	kde4-libkdcraw < 4.6.99
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
Obsoletes:	kde4-libkdcraw-devel < 4.6.99

%description devel
Header files for libkdcraw development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających libkdcraw.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
		../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkdcraw.so.??
%attr(755,root,root) %{_libdir}/libkdcraw.so.*.*.*
%{_datadir}/apps/libkdcraw
%{_iconsdir}/hicolor/*x*/apps/kdcraw.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdcraw.so
%{_includedir}/libkdcraw
%{_pkgconfigdir}/libkdcraw.pc
