from absl.testing import absltest

import configurable
import dataset
import vocab


class DatasetTest(absltest.TestCase):

  def test_dataset(self):
    config = configurable.Configurable(config_file='test_data/test.cfg')

    vocab_files = [(config.word_file, 1, 'Words'),
                   (config.tag_file, [3, 4], 'Tags'),
                   (config.rel_file, 7, 'Rels')]
    vocabs = []
    for i, (vocab_file, index, name) in enumerate(vocab_files):
      vocabs.append(
          vocab.Vocab(
              vocab_file,
              index,
              name=name,
              cased=config.cased if not i else True,
              use_pretrained=(not i),
              config_file='test_data/test.cfg'))

    ds = dataset.Dataset(
        config.train_file,
        vocabs,
        lambda: None,
        config_file='test_data/test.cfg')

    # the number of buckets and the number of sentences.
    self.assertEqual(len(ds), 3)
    self.assertEqual(list(len(b) for b in ds), [4, 4, 3])


if __name__ == '__main__':
  absltest.main()
