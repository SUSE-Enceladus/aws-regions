#
# spec file for package aws-regions
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python3-aws-regions
Version:        0.0.3
Release:        0
Summary:        API for retrieving the most up-to-date AWS region list
License:        MIT
URL:            https://github.com/SUSE-Enceladus/aws-regions
Source:         https://files.pythonhosted.org/packages/source/a/aws-regions/aws-regions-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-requests
BuildRequires:  python3-pytest
BuildRequires:  python3-vcrpy
Requires:       python3-requests

%description

%prep
%setup -q -n aws-regions-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
python3 -m pytest

%files
%doc python3-aws-regions.changes README.md
%{python3_sitelib}/*

%changelog

