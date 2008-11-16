Name:		merkaartor
Version:	0.12
Release:	%mkrel 1
License:	GPLv2+
URL:		http://qmmp.ylsoftware.com/index_en.php
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel >= 4.4
BuildRequires:	qt4-linguist
BuildRequires:	libexiv-devel
Source:		http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2
Group:		Sciences/Other
Summary:	Openstreetmap mapping program

%description
Merkaartor is an openstreetmap (http://www.openstreetmap.org) mapping
program. Merkaartor focuses on providing a visually pleasing but
performant editing environment for free geographical data.

%prep
%setup -q

%build
lrelease Merkaartor.pro
%qmake_qt4 \
	TRANSDIR_MERKAARTOR=%_datadir/merkaartor/translations \
	TRANSDIR_SYSTEM=%qt4dir/translations \
	PREFIX=%_prefix \
	GDAL=1
%make

%install
rm -rf %buildroot
make install INSTALL_ROOT=%buildroot

mkdir -p %buildroot%_datadir/applications
cat >%buildroot%_datadir/applications/mandriva-%name.desktop <<EOF
[Desktop Entry]
Name=merkaartor
Comment=Openstreetmap client
Exec=%_bindir/%name
Icon=geosciences_section
Terminal=false
Type=Application
StartupNotify=true
Categories=Geoscience;Qt;Science;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%_datadir/%name
%_datadir/applications/*.desktop
