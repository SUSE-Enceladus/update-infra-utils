#
# spec file for package enable-rmt-repos
#
# Copyright (c) 2019 SUSE Linux GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           enable-rmt-repos
Version:        4.0.1
Release:        0
Summary:        RMT repository enablement
License:        GPL-3.0+
Group:          System/Management
Url:            https://github.com/pubcloud
Source:         %{name}-%{version}.tar.bz2
Requires:       enable-rmt-repos-conf >= 2.0
Requires:       python3
Requires:       rmt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
RMT repository enablement.

%prep
%setup -q -n %{name}-%{version}

%build

%install
make install-exec DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_sbindir}/enable-rmt-repos

%changelog
