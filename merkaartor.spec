Name:		merkaartor
Version:	0.17.2
Release:	%mkrel 1
License:	GPLv2+
URL:		http://www.merkaartor.org
BuildRequires:	qt4-devel >= 4.4
BuildRequires:	qt4-linguist
BuildRequires:	libexiv-devel gdal-devel
BuildRequires:	boost-devel
Source0:	http://www.merkaartor.org/downloads/source/%{name}-%{version}.tar.bz2
Group:		Sciences/Other
Summary:	Openstreetmap mapping program

%description
Merkaartor is an openstreetmap (http://www.openstreetmap.org) mapping
program. Merkaartor focuses on providing a visually pleasing but
performant editing environment for free geographical data.

%prep
%setup -q

%build
lrelease translations/merkaartor*.ts
%qmake_qt4 \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	TRANSDIR_MERKAARTOR=%_datadir/%{name}/translations \
	TRANSDIR_SYSTEM=%qt4dir/translations \
	GDAL=1
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt
rm -f %{buildroot}/merkaartor.gdb-index

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%_datadir/%{name}/*.xml
%_datadir/%{name}/world_background.osb
%_datadir/applications/*.desktop
%{_libdir}/%{name}/plugins/background/*.so
%{_libdir}/%{name}/plugins/styles/libskulpture.so
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%doc AUTHORS CHANGELOG CREDITS TODO
