Name: qedje
Version: 0.4.0
Release: 9
License: GPL
Group: Development/KDE and Qt 
Summary: QEdje - Declarative language
Source: %name-%version.tar.gz
Patch0:       qedje-0.4.0-fix-install.patch
Url: http://code.openbossa.org/projects/qedje
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel
BuildRequires: kde4-macros
BuildRequires: qzion-devel >= 0.4.0
BuildRequires: eet-devel

%description
Edje is a declarative language that simplifies the development of 
complex interfaces separating the UI design from the application 
logic, by providing animations, layouts and simple scripts in a 
very small memory footprint.

%files
%defattr(-,root,root)
%_kde_bindir/qedje_viewer

#------------------------------------------------

%define libqedje_major 0
%define libqedje %mklibname qedje %{libqedje_major}

%package -n %libqedje
Summary: qedjelibrary
Group: System/Libraries

%description -n %libqedje
qedje library.


%files -n %libqedje
%defattr(-,root,root)
%_kde_libdir/libqedje.so.%{libqedje_major}*

#-----------------------------------------------

%package   devel
Summary:   Devel stuff for kdebase 4
Group:     Development/KDE and Qt
Requires:  %libqedje = %version

%description  devel
Devel packages needed to build qedje apps

%files devel
%defattr(-,root,root)
%_kde_includedir/*.h
%_kde_libdir/pkgconfig/qedje.pc
%_kde_libdir/libqedje.so

#------------------------------------------------

%prep
%setup -q -n %name-mainline
%patch0 -p1

%build
%cmake_qt4 -DBUILD_TOOLS=TRUE
%make

%install
rm -rf %{buildroot}
cd build
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-7mdv2011.0
+ Revision: 669379
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-6mdv2011.0
+ Revision: 607262
- rebuild

* Wed Mar 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.0-4mdv2010.1
+ Revision: 524162
- Fix install with new cmake

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for 2010.1

* Tue Jul 07 2009 Helio Chissini de Castro <helio@mandriva.com> 0.4.0-2mdv2010.0
+ Revision: 393182
- Rebuild against new eet

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 0.4.0-1mdv2009.1
+ Revision: 345904
- Update with new upstream final 0.4.0 package

* Sun Dec 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.0-0.20081023.4mdv2009.1
+ Revision: 316948
- Fix Requires

* Sun Dec 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.0-0.20081023.3mdv2009.1
+ Revision: 316847
- Rebuild  because of missing package

* Fri Oct 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.4.0-0.20081023.2mdv2009.1
+ Revision: 296894
- improve BuildRequires
- import qedje


