Name:		merkaartor
Version:	0.15.3
Release:	%mkrel 2
License:	GPLv2+
URL:		http://www.merkaartor.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel >= 4.4
BuildRequires:	qt4-linguist
BuildRequires:	libexiv-devel gdal-devel
Source:		http://www.merkaartor.org/downloads/source/%{name}-%{version}.tar.bz2
Patch0:		merkaartor-0.14-strfmt.patch
Group:		Sciences/Other
Summary:	Openstreetmap mapping program

%description
Merkaartor is an openstreetmap (http://www.openstreetmap.org) mapping
program. Merkaartor focuses on providing a visually pleasing but
performant editing environment for free geographical data.

%prep
%setup -q
#%patch0 -p1 -b .fmtstr

%build
lrelease Merkaartor.pro
%qmake_qt4 \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	TRANSDIR_MERKAARTOR=%_datadir/merkaartor/translations \
	TRANSDIR_SYSTEM=%qt4dir/translations \
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
%{_libdir}/%{name}/plugins/background/*.so
%{_libdir}/%{name}/plugins/styles/libskulpture.so
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

