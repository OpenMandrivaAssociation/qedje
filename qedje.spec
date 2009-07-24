Name: qedje
Version: 0.4.0
Release: %mkrel 2
License: GPL
Group: Development/KDE and Qt 
Summary: QEdje - Declarative language
Source: %name-%version.tar.gz
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

%build
%cmake_qt4 -DBUILD_TOOLS=TRUE
%make

%install
rm -rf %{buildroot}
cd build
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot
