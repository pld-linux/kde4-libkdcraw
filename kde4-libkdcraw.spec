Summary:	KDcraw libary
Summary(pl.UTF-8):	Biblioteka KDcraw
Name:		libkdcraw
Version:	0.1.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/kipi/%{name}-%{version}.tar.bz2
# Source0-md5:	46108744a7d8b0b9b0eaa9737c5e1fba
URL:		http://extragear.kde.org/apps/kipi/
Patch0:		kde-ac260-lt.patch
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

#%package static
#Summary:	Static libkdcraw library
#Summary(pl.UTF-8):	Biblioteka statyczna libkdcraw
#Group:		Development/Libraries
#Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

#%description static
#Static libkdcraw library.

#%description static -l pl.UTF-8
#Biblioteka statyczna libkdcraw.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.?.?.?
%{_iconsdir}/hicolor/*x*/*/*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/libkdcraw

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/lib*.a
