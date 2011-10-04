# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.19
# 
# >> macros
# << macros

Name:       xorg-x11-proto-kbproto
Summary:    X.Org X11 Protocol kbproto
Version:    1.0.5
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/kbproto-%{version}.tar.bz2
Source100:  xorg-x11-proto-kbproto.yaml
BuildRequires:  pkgconfig(xorg-macros)
Provides:   kbproto


%description
Description: %{summary}



%prep
%setup -q -n kbproto-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%reconfigure --disable-static \
    --libdir=%{_datadir}

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install 

# >> install post
# << install post






%files
%defattr(-,root,root,-)
# >> files
%{_datadir}/pkgconfig/kbproto.pc
%{_includedir}/X11/extensions/XKB.h
%{_includedir}/X11/extensions/XKBsrv.h
%{_includedir}/X11/extensions/XKBproto.h
%{_includedir}/X11/extensions/XKBstr.h
%{_includedir}/X11/extensions/XKBgeom.h
# << files


