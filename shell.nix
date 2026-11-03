{ pkgs ? import <nixpkgs> {
    config.allowUnfree = true;
  }
}:

pkgs.mkShell {
  packages = with pkgs; [
    python312
    uv
    # git
    # gcc
    # pkg-config

    ruff
    basedpyright
    unzip
  ];

}

